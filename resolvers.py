import graphene
from db import users, posts, comments, follows, likes, messages
from datetime import datetime

class UserType(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    email = graphene.String()
    bio = graphene.String()
    avatar_url = graphene.String()
    join_date = graphene.String()
    posts = graphene.List(lambda: PostType)
    followers_count = graphene.Int()
    following_count = graphene.Int()
    followers = graphene.List(lambda: UserType)
    following = graphene.List(lambda: UserType)

    def resolve_posts(parent, info):
        return [p for p in posts if p["user_id"] == parent["id"]]

    def resolve_followers_count(parent, info):
        return len([f for f in follows if f["following_id"] == parent["id"]])

    def resolve_following_count(parent, info):
        return len([f for f in follows if f["follower_id"] == parent["id"]])

    def resolve_followers(parent, info):
        follower_ids = [f["follower_id"] for f in follows if f["following_id"] == parent["id"]]
        return [u for u in users if u["id"] in follower_ids]

    def resolve_following(parent, info):
        following_ids = [f["following_id"] for f in follows if f["follower_id"] == parent["id"]]
        return [u for u in users if u["id"] in following_ids]

class PostType(graphene.ObjectType):
    id = graphene.ID()
    content = graphene.String()
    image_url = graphene.String()
    created_at = graphene.String()
    likes_count = graphene.Int()
    comments_count = graphene.Int()
    user = graphene.Field(UserType)
    comments = graphene.List(lambda: CommentType)

    def resolve_user(parent, info):
        return next((u for u in users if u["id"] == parent["user_id"]), None)

    def resolve_comments(parent, info):
        return [c for c in comments if c["post_id"] == parent["id"]]

    def resolve_comments_count(parent, info):
        return len([c for c in comments if c["post_id"] == parent["id"]])

class CommentType(graphene.ObjectType):
    id = graphene.ID()
    content = graphene.String()
    created_at = graphene.String()
    user = graphene.Field(UserType)
    post = graphene.Field(PostType)

    def resolve_user(parent, info):
        return next((u for u in users if u["id"] == parent["user_id"]), None)

    def resolve_post(parent, info):
        return next((p for p in posts if p["id"] == parent["post_id"]), None)

class MessageType(graphene.ObjectType):
    id = graphene.ID()
    content = graphene.String()
    sent_at = graphene.String()
    read_at = graphene.String()
    sender = graphene.Field(UserType)
    receiver = graphene.Field(UserType)

    def resolve_sender(parent, info):
        return next((u for u in users if u["id"] == parent["sender_id"]), None)

    def resolve_receiver(parent, info):
        return next((u for u in users if u["id"] == parent["receiver_id"]), None)

class FollowerType(graphene.ObjectType):
    user = graphene.Field(UserType)
    created_at = graphene.String()

class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, username=graphene.String(required=True))
    feed = graphene.List(PostType, user_id=graphene.ID(required=True))
    followers = graphene.List(FollowerType, user_id=graphene.ID(required=True))

    def resolve_users(parent, info):
        return users

    def resolve_user(parent, info, username):
        return next((u for u in users if u["username"] == username), None)

    def resolve_feed(parent, info, user_id):
        following_ids = [f["following_id"] for f in follows if f["follower_id"] == user_id]
        return [p for p in posts if p["user_id"] in following_ids]

    def resolve_followers(parent, info, user_id):
        followers_data = [f for f in follows if f["following_id"] == user_id]
        result = []
        for f in followers_data:
            user = next((u for u in users if u["id"] == f["follower_id"]), None)
            result.append({
                "user": user,
                "created_at": f["created_at"]
            })
        return result

class CreatePostInput(graphene.InputObjectType):
    user_id = graphene.ID(required=True)
    content = graphene.String(required=True)
    image_url = graphene.String()

class CreatePost(graphene.Mutation):
    class Arguments:
        input = CreatePostInput(required=True)

    post = graphene.Field(PostType)

    def mutate(parent, info, input):
        new_post = {
            "id": str(len(posts) + 1),
            "user_id": input["user_id"],
            "content": input["content"],
            "image_url": input.get("image_url"),
            "created_at": datetime.now().isoformat(),
            "likes_count": 0
        }
        posts.append(new_post)
        return CreatePost(post=new_post)

class LikePostInput(graphene.InputObjectType):
    user_id = graphene.ID(required=True)
    post_id = graphene.ID(required=True)

class LikePost(graphene.Mutation):
    class Arguments:
        input = LikePostInput(required=True)

    likes_count = graphene.Int()
    post = graphene.Field(PostType)

    def mutate(parent, info, input):
        user_id = input["user_id"]
        post_id = input["post_id"]
        
        post = next((p for p in posts if p["id"] == post_id), None)
        if not post:
            raise Exception("Post not found")
            
        existing_like = next((l for l in likes if l["user_id"] == user_id and l["post_id"] == post_id), None)
        if not existing_like:
            likes.append({
                "user_id": user_id,
                "post_id": post_id,
                "created_at": datetime.now().isoformat()
            })
            post["likes_count"] += 1
            
        return LikePost(likes_count=post["likes_count"], post=post)

class CreateCommentInput(graphene.InputObjectType):
    user_id = graphene.ID(required=True)
    post_id = graphene.ID(required=True)
    content = graphene.String(required=True)

class CreateComment(graphene.Mutation):
    class Arguments:
        input = CreateCommentInput(required=True)

    comment = graphene.Field(CommentType)

    def mutate(parent, info, input):
        new_comment = {
            "id": str(len(comments) + 1),
            "post_id": input["post_id"],
            "user_id": input["user_id"],
            "content": input["content"],
            "created_at": datetime.now().isoformat()
        }
        comments.append(new_comment)
        return CreateComment(comment=new_comment)

class FollowUserInput(graphene.InputObjectType):
    follower_id = graphene.ID(required=True)
    following_id = graphene.ID(required=True)

class FollowUser(graphene.Mutation):
    class Arguments:
        input = FollowUserInput(required=True)

    follower = graphene.Field(UserType)
    following = graphene.Field(UserType)

    def mutate(parent, info, input):
        f_id = input["follower_id"]
        t_id = input["following_id"]
        if f_id == t_id:
            raise Exception("Cannot follow yourself")
            
        existing = next((f for f in follows if f["follower_id"] == f_id and f["following_id"] == t_id), None)
        if not existing:
            follows.append({
                "follower_id": f_id,
                "following_id": t_id,
                "created_at": datetime.now().isoformat()
            })
        
        follower = next((u for u in users if u["id"] == f_id), None)
        following = next((u for u in users if u["id"] == t_id), None)
        return FollowUser(follower=follower, following=following)

class SendMessageInput(graphene.InputObjectType):
    sender_id = graphene.ID(required=True)
    receiver_id = graphene.ID(required=True)
    content = graphene.String(required=True)

class SendMessage(graphene.Mutation):
    class Arguments:
        input = SendMessageInput(required=True)

    message = graphene.Field(MessageType)

    def mutate(parent, info, input):
        new_msg = {
            "id": str(len(messages) + 1),
            "sender_id": input["sender_id"],
            "receiver_id": input["receiver_id"],
            "content": input["content"],
            "sent_at": datetime.now().isoformat()
        }
        messages.append(new_msg)
        return SendMessage(message=new_msg)

class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    like_post = LikePost.Field()
    create_comment = CreateComment.Field()
    follow_user = FollowUser.Field()
    send_message = SendMessage.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

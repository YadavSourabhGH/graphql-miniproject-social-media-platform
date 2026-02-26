# Social Media Platform - GraphQL API Documentation

## 🎯 Goal
Create a GraphQL API for a social media platform where users can create profiles, post content, follow others, and interact with posts.

---

## 🏗 Database Models
The system uses the following core models (implemented in `db.py`):

- **User**: `id`, `username`, `email`, `bio`, `avatarUrl`, `joinDate`
- **Post**: `id`, `userId`, `content`, `imageUrl`, `createdAt`, `likesCount`
- **Comment**: `id`, `postId`, `userId`, `content`, `createdAt`
- **Follow**: `followerId`, `followingId`, `createdAt` (junction table)
- **Like**: `userId`, `postId`, `createdAt` (junction table)
- **Message**: `id`, `senderId`, `receiverId`, `content`, `sentAt`, `readAt`

---

## 🔍 Test Queries

### 1. Get User Profile with Posts
```graphql
query {
  user(username: "alex_explorer") {
    id
    username
    bio
    posts {
      content
      likesCount
      comments { content }
    }
    followersCount
    followingCount
  }
}
```

### 2. Get Feed for User
```graphql
query {
  feed(userId: "4") {
    id
    content
    user { username, avatarUrl }
    likesCount
    comments { content }
  }
}
```

### 3. Get Followers List
```graphql
query {
  followers(userId: "1") {
    user { username }
    createdAt
  }
}
```

---

## ⚡ Test Mutations

### 1. Create a Post
```graphql
mutation {
  createPost(input: {
    userId: "1"
    content: "Hello World!"
    imageUrl: "https://example.com/image.jpg"
  }) {
    post {
      id
      content
      createdAt
    }
  }
}
```

### 2. Like a Post
```graphql
mutation {
  likePost(input: {
    userId: "1"
    postId: "1"
  }) {
    likesCount
    post {
      id
      likesCount
    }
  }
}
```

---

## ✅ Expected Test Cases
1. User profile shows posts and followers
2. Feed shows posts from followed users
3. Like increments count correctly
4. Follow creates bidirectional relationship
5. Comments added to posts correctly
6. Messages sent and received
7. Post shows correct like/comment counts

---

## 💡 Hints & Implementation Notes
- **Followers**: Implemented as a many-to-many relationship using a junction data structure.
- **Likes**: Tracked on posts to provide real-time `likesCount`.
- **Communication**: Full message system for direct user interaction.
- **Aggregations**: Dynamic calculation of like and comment counts.

---

## 🚀 How to Test
1. Run the server: `python main.py`
2. Open the browser to: `http://localhost:8000/`
3. Copy and paste the queries above into the GraphiQL editor.

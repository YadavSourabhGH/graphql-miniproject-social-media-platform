import requests
import json

def query(q, variables=None):
    url = 'http://localhost:8000/'
    try:
        response = requests.post(url, json={'query': q, 'variables': variables})
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Query failed with status code {response.status_code}: {response.text}")
            return None
    except Exception as e:
        print(f"Connection error: {e}")
        return None

def run_tests():
    print("--- TEST 1: Get User Profile (Alex Explorer) ---")
    user_query = """
    query {
      user(username: "alex_explorer") {
        username
        bio
        posts {
          content
          likesCount
          commentsCount
        }
        followersCount
        followingCount
      }
    }
    """
    res = query(user_query)
    if res: print(json.dumps(res, indent=2))

    print("\n--- TEST 2: Get Feed for Luna Travels (User ID 4) ---")
    feed_query = """
    query {
      feed(userId: "4") {
        content
        user { username }
        likesCount
      }
    }
    """
    res = query(feed_query)
    if res: print(json.dumps(res, indent=2))

    print("\n--- TEST 3: Create New Post for Sara ---")
    create_post_mutation = """
    mutation {
      createPost(input: {
        userId: "2"
        content: "Just finished building this social media API with Python and GraphQL! 🐍✨"
      }) {
        post {
          id
          content
          createdAt
        }
      }
    }
    """
    res = query(create_post_mutation)
    if res: print(json.dumps(res, indent=2))

    print("\n--- TEST 4: Like Alex's Mountain Post ---")
    like_post_mutation = """
    mutation {
      likePost(input: {
        userId: "4"
        postId: "1"
      }) {
        likesCount
        post {
          id
          likesCount
        }
      }
    }
    """
    res = query(like_post_mutation)
    if res: print(json.dumps(res, indent=2))

    print("\n--- TEST 5: Message Between Users ---")
    msg_mutation = """
    mutation {
      sendMessage(input: {
        senderId: "3"
        receiverId: "1"
        content: "Alex, let's go climbing next weekend! I'll bring some gourmet snacks."
      }) {
        message {
          content
          sender { username }
          receiver { username }
        }
      }
    }
    """
    res = query(msg_mutation)
    if res: print(json.dumps(res, indent=2))

if __name__ == "__main__":
    run_tests()

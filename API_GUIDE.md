# Social Media API - GraphQL Guide

This guide provides a comprehensive list of all available Queries and Mutations for the Social Media Platform API.

## 🚀 Getting Started

1. Start the server: `python main.py`
2. Open the GraphQL Playground: `http://localhost:8000/`

---

## 🔍 Queries (Data Retrieval)

### 1. Get User Profile
Fetches a user's basic info, their posts, and follow counts.
```graphql
query {
  user(username: "alex_explorer") {
    id
    username
    bio
    avatarUrl
    joinDate
    posts {
      content
      likesCount
      commentsCount
    }
    followersCount
    followingCount
  }
}
```

### 2. Get User Feed
Shows posts from people that a specific user follows.
```graphql
query {
  feed(userId: "4") {
    id
    content
    imageUrl
    createdAt
    likesCount
    commentsCount
    user {
      username
    }
  }
}
```

### 3. Get Followers List
Lists everyone following a specific user and the follow date.
```graphql
query {
  followers(userId: "1") {
    user {
      username
      avatarUrl
    }
    createdAt
  }
}
```

### 4. List All Users
A quick overview of all registered users in the system.
```graphql
query {
  users {
    id
    username
    email
  }
}
```

---

## ⚡ Mutations (Actions)

### 1. Create a New Post
Add new content to a user's profile.
```graphql
mutation {
  createPost(input: {
    userId: "2",
    content: "Building with FastAPI and Graphene is so efficient! 🐍🚀",
    imageUrl: "https://images.unsplash.com/photo-1517694712202-14dd9538aa97"
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
Increments the `likesCount` for a specific post.
```graphql
mutation {
  likePost(input: {
    userId: "3",
    postId: "2"
  }) {
    likesCount
    post {
      id
      content
    }
  }
}
```

### 3. Add a Comment
Post feedback on an existing post.
```graphql
mutation {
  createComment(input: {
    userId: "4",
    postId: "3",
    content: "This bread looks incredible! Can't wait to try the recipe."
  }) {
    comment {
      id
      content
      createdAt
      user {
        username
      }
    }
  }
}
```

### 4. Follow a User
Establish a new follow connection between two users.
```graphql
mutation {
  followUser(input: {
    followerId: "3",
    followingId: "4"
  }) {
    follower {
      username
      followingCount
    }
    following {
      username
      followersCount
    }
  }
}
```

### 5. Send a Private Message
Simulate a direct message between two users.
```graphql
mutation {
  sendMessage(input: {
    senderId: "1",
    receiverId: "4",
    content: "Hey Luna! Welcome to the adventure club! 🧗‍♂️"
  }) {
    message {
      id
      content
      sentAt
      sender { username }
      receiver { username }
    }
  }
}
```

---

## 🛠 Tech Stack Details

- **Backend**: FastAPI (Python)
- **GraphQL**: Graphene
- **Mock Data**: Pre-populated in `db.py`
- **Logic**: Implemented in `resolvers.py`

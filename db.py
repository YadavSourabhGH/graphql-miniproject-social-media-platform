from datetime import datetime

users = [
    {
        "id": "1",
        "username": "alex_explorer",
        "email": "alex@adventure.com",
        "bio": "Mountain climber | Nature lover | Coffee addict ☕️",
        "avatar_url": "https://i.pravatar.cc/150?u=alex",
        "join_date": "2023-05-12T10:30:00Z"
    },
    {
        "id": "2",
        "username": "sara_codes",
        "email": "sara@tech.io",
        "bio": "Full-stack developer | Open source contributor | 💻 & 🍵",
        "avatar_url": "https://i.pravatar.cc/150?u=sara",
        "join_date": "2023-06-20T14:45:00Z"
    },
    {
        "id": "3",
        "username": "mike_chef",
        "email": "mike@gourmet.com",
        "bio": "Life is too short for bad food. 🍳 | Recipe creator",
        "avatar_url": "https://i.pravatar.cc/150?u=mike",
        "join_date": "2023-08-05T09:15:00Z"
    },
    {
        "id": "4",
        "username": "luna_travels",
        "email": "luna@globe.com",
        "bio": "Exploring the world one city at a time. ✈️🌍",
        "avatar_url": "https://i.pravatar.cc/150?u=luna",
        "join_date": "2023-11-30T16:20:00Z"
    }
]

posts = [
    {
        "id": "1",
        "user_id": "1",
        "content": "Just reached the summit of Mt. Rainier! The view is absolutely breathtaking. 🏔️",
        "image_url": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b",
        "created_at": "2024-01-15T08:00:00Z",
        "likes_count": 124
    },
    {
        "id": "2",
        "user_id": "2",
        "content": "Finally migrated my entire project to GraphQL. The developer experience is night and day! 🚀",
        "image_url": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97",
        "created_at": "2024-02-01T11:30:00Z",
        "likes_count": 89
    },
    {
        "id": "3",
        "user_id": "3",
        "content": "Making homemade sourdough today. The crust is perfect! 🥖😋",
        "image_url": "https://images.unsplash.com/photo-1585478259715-876a6a81fc08",
        "created_at": "2024-02-10T15:45:00Z",
        "likes_count": 56
    },
    {
        "id": "4",
        "user_id": "4",
        "content": "A beautiful sunset in Santorini. 🌅 Missing the Greek summer.",
        "image_url": "https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff",
        "created_at": "2024-02-20T19:10:00Z",
        "likes_count": 210
    }
]

comments = [
    {
        "id": "1",
        "post_id": "1",
        "user_id": "2",
        "content": "Incredible shot! Be safe coming down.",
        "created_at": "2024-01-15T09:30:00Z"
    },
    {
        "id": "2",
        "post_id": "2",
        "user_id": "1",
        "content": "GraphQL is the way to go! Welcome to the club.",
        "created_at": "2024-02-01T12:15:00Z"
    },
    {
        "id": "3",
        "post_id": "3",
        "user_id": "4",
        "content": "That bread looks amazing! Can you share the recipe?",
        "created_at": "2024-02-10T16:20:00Z"
    }
]

follows = [
    {"follower_id": "1", "following_id": "2", "created_at": "2023-12-01T10:00:00Z"},
    {"follower_id": "2", "following_id": "1", "created_at": "2023-12-05T14:30:00Z"},
    {"follower_id": "3", "following_id": "1", "created_at": "2024-01-01T09:00:00Z"},
    {"follower_id": "4", "following_id": "1", "created_at": "2024-01-10T11:00:00Z"},
    {"follower_id": "4", "following_id": "2", "created_at": "2024-01-12T12:00:00Z"},
    {"follower_id": "4", "following_id": "3", "created_at": "2024-01-15T15:00:00Z"}
]

likes = [
    {"user_id": "2", "post_id": "1", "created_at": "2024-01-15T08:30:00Z"},
    {"user_id": "3", "post_id": "1", "created_at": "2024-01-15T09:00:00Z"},
    {"user_id": "1", "post_id": "2", "created_at": "2024-02-01T12:00:00Z"}
]

messages = [
    {
        "id": "1",
        "sender_id": "1",
        "receiver_id": "2",
        "content": "Hey Sara, saw you switched to GraphQL. How do you like it?",
        "sent_at": "2024-02-01T13:00:00Z",
        "read_at": "2024-02-01T13:05:00Z"
    },
    {
        "id": "2",
        "sender_id": "2",
        "receiver_id": "1",
        "content": "It's amazing! Saving so much time on API documentation.",
        "sent_at": "2024-02-01T13:10:00Z",
        "read_at": None
    }
]

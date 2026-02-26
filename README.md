# Social Media GraphQL API (FastAPI + Graphene)

This is a GraphQL API for a social media platform, built with **Python**, **FastAPI**, and **Graphene**.

## Features

- **Users**: Profiles, followers, following.
- **Posts**: Create posts, like posts, feed.
- **Comments**: Comment on posts.
- **Messages**: Send and receive private messages.

## Tech Stack

- **Framework**: FastAPI
- **GraphQL**: Graphene
- **Server**: Uvicorn
- **Integration**: Starlette-Graphene

## Project Structure

- `db.py`: In-memory data store with realistic mock data.
- `resolvers.py`: GraphQL Types, Queries, and Mutations using Graphene.
- `main.py`: FastAPI application serving the GraphQL endpoint.
- `verify_py.py`: Integration test script.

## Getting Started

1. **Set up virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the server**:
   ```bash
   python main.py
   ```
   The server will run at `http://localhost:8000/`.

4. **Run verification script**:
   ```bash
   python verify_py.py
   ```

## GraphQL Playground

Open `http://localhost:8000/` in your browser to explore the API using the built-in GraphQL Playground.

For a full list of available queries and mutations, see the [API_GUIDE.md](file:///Users/sourabhyadav/Downloads/graphql-miniproject/API_GUIDE.md).

### Realistic Data Included
The system comes pre-populated with realistic users like `alex_explorer`, `sara_codes`, `mike_chef`, and `luna_travels`, including posts, comments, and follow relationships.

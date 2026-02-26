from fastapi import FastAPI
from starlette_graphene import GraphQLApp
from resolvers import schema

app = FastAPI()

app.add_route("/", GraphQLApp(schema=schema))

if __name__ == "__main__":
    import uvicorn
    print("🚀 Server ready at http://localhost:8000/")
    uvicorn.run(app, host="0.0.0.0", port=8000)

import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"

    @strawberry.field
    def bye(self) -> str:
        return "Goodbye World"


@strawberry.type
class Mutation:
    @strawberry.mutation
    def thousand(self, number: int) -> int:
        return number * 1000

    @strawberry.mutation
    def hundred(self, number: int) -> int:
        return number * 100


schema = strawberry.Schema(Query, Mutation)

graphql_app = GraphQLRouter(schema)

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello World"}


app.include_router(graphql_app, prefix="/graphql")


if __name__ == "__main__":
    import uvicorn

    # デバッグ用。python main.pyで起動することはproductionではおこなわわれない
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=True,
        port=5678,
    )

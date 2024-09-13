from fastapi import FastAPI
from controllers.order_controller import order_router

app = FastAPI()

# Register order routes
app.include_router(order_router)

# Run the application (when using uvicorn)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

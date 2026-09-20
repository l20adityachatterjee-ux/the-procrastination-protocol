from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="The Procrastination Protocol API")

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class DeviceAssessment(BaseModel):
    is_repairable: bool
    is_reusable: bool
    is_refurbishable: bool

@app.post("/api/assess")
def assess_device(data: DeviceAssessment):
    # Core Decision Tree Logic
    if data.is_repairable:
        pathway = "Repair"
    elif data.is_reusable:
        pathway = "Reuse / Resale"
    elif data.is_refurbishable:
        pathway = "Refurbishment"
    else:
        pathway = "Responsible Recycling"
        
    return {"recommended_pathway": pathway}
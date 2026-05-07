from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from enum import Enum

class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class RoutingDecision(str, Enum):
    SEND = "send"
    ASK_MORE = "ask_more"
    ESCALATE = "escalate"

class QueryRequest(BaseModel):
    query: str = Field(..., example="I want to check my balance")
    session_id: Optional[str] = None

class IntentResult(BaseModel):
    intent: str
    confidence: float

class PriorityResult(BaseModel):
    level: Priority
    reason: str

class PolicyResult(BaseModel):
    policy_snippet: str
    source: str

class DraftResult(BaseModel):
    draft_response: str
    missing_information: List[str] = []
    next_action: Optional[str] = None

class ValidationResult(BaseModel):
    is_valid: bool
    feedback: Optional[str] = None

class RouterResult(BaseModel):
    decision: RoutingDecision
    explanation: str

class AgentTrace(BaseModel):
    intent: Optional[IntentResult] = None
    priority: Optional[PriorityResult] = None
    policy: Optional[PolicyResult] = None
    draft: Optional[DraftResult] = None
    validation: Optional[ValidationResult] = None
    router: Optional[RouterResult] = None

class QueryResponse(BaseModel):
    query: str
    response: str
    trace: AgentTrace

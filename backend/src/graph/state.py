import operator
from typing import Annotated,List,Dict,Optional,Any,TypedDict

# schema for a single compliance result
#error Report

class ComplianceIssue(TypedDict):
    category : str 
    description : str # specific detail of violation
    severity : str #Critical | Warning
    timestamp : Optional[str] 
    
    
# define the global graph state
# this defines the sate that gets passed around in the agentic workflow
class VideoAuditState(TypedDict):
    '''
    Defines the data schema for langgraph execution content
    Main container : holds all the information about the audit
    right from the initial URL to the final report 
    '''
    #input parameters
    video_url : str
    video_id : str
    
    #ingestion and extraction data
    local_file_path : Optional[str]
    video_metadata : Dict[str,Any] # {"duration":15, "resolution" : "1080p"}
    transcript : Optional[str] # FUlly extracted speech to text
    ocr_text : List[str]
    
    #analysis output
    compliance_results : Annotated[List[ComplianceIssue] , operator.add]
    
    #final_deliverables:
    
    final_status : str #PASS | FAIL
    final_report : str #markdown format
    
    #system observability
    # errors : API timeout, system level errors
    
    errors : Annotated[List[str],operator.add]
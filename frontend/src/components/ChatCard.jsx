import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

function ChatCard(){
    return (
        <div>
            <a href="#" className="list-group-item list-group-item-action">
                <div className="d-flex align-items-center">
                        <div className="avatar bg-primary text-white rounded-circle d-flex align-items-center justify-content-center me-2" 
                                style={{width:"40px", height:"40px", fontSize:"30px"}}>
                            A
                        </div>                                
                    Ashenafi
                </div>
            </a>
        </div>
    );
}

export default ChatCard;
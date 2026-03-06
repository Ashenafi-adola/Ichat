
import ChatCard from './ChatCard';

function SideBar(){
    return (
        <div className="col-md-4 col-lg-3 border-end d-flex flex-column collapse d-md-block" id="sidebar">
            <div class="p-3 flex-grow-1 overflow-auto">
                <h3 class="h5">Chats</h3>
                <hr />
                
                
                <div class="list-group list-group-flush">
                    <ChatCard/>
                </div>
            </div>
        </div>
    )
}

export default SideBar;
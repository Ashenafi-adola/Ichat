
import ChatCard from './ChatCard';

function SideBar(){
    return (        
       <div className="col-md-4 col-lg-3 border-end d-flex flex-column collapse d-md-block p-0" style={{minWidth:"200px", margin:"0px"}} id="sidebar">
            <div className="p-1 flex-grow-1 overflow-auto">
                <div className='card-header'>
                    <form action="">
                        <div class="input-group mb-3">
                            <input type="text" className="form-control" placeholder="Search..." aria-label="Recipient’s username" aria-describedby="button-addon2"/>
                            <button className="btn btn-outline-secondary" type="button" id="button-addon2">Search</button>
                        </div>
                    </form>
                </div>
                <hr style={{height:"1px", margin:"2px"}}/>
                <div className="list-group list-group-flush overflow-auto pb-5 " style={{maxHeight:"calc(100vh - 130px)", scrollbarWidth: "none", padding:'0px'}}>
                    <ChatCard/>
                    <ChatCard/>
                    <ChatCard/>
                    <ChatCard/>
                    <ChatCard/>
                    <ChatCard/>
                    <ChatCard/>
                    <ChatCard/>
                    <ChatCard/>
                    <ChatCard/>
                    <ChatCard/>
                    <ChatCard/>
                    <ChatCard/>
                    <ChatCard/>
                    <ChatCard/>
                </div>
            </div>
        </div>
    )
}

export default SideBar;
import { useState } from 'react';
import ChatArea from './ChatArea'

function SideBar(){
    const [sidebarOpen, setSidebarOpen] = useState(false);

    const toggleSidebar = () => {
        setSidebarOpen(!sidebarOpen);
    };
    return (
        <div className="container-fluid vh-100">
            <hr />
            <hr />
            <hr />
            <div className="row h-100">
                <div className={`col-md-4 col-lg-3 border-end d-flex flex-column collapse d-md-block ${sidebarOpen ? 'show' : ''}`} id="sidebar">
                    <div class="p-3 flex-grow-1 overflow-auto">
                      <h3 class="h5">Chats</h3>
                      <hr />
                        
                        
                        <div class="list-group list-group-flush">
                            
                        </div>
                    </div>
                </div>
                <div class="col-md-8 col-lg-9 d-flex flex-column">
                    <div class="flex-grow-1 d-flex flex-column">
                        <ChatArea/>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default SideBar;
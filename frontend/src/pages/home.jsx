import ChatList from "../components/chatList";
import SideBar from "../components/SideBar";
import ChatArea from "../components/ChatArea";
import { useState } from "react";
function Home() {
    const [sidebarOpen, setSidebarOpen] = useState(false);

    return (
        <div className="container-fluid vh-100">
            <hr />
            <hr />
            <hr />
            <div className="row h-100">
                <SideBar/>
                <div class="col-md-8 col-lg-9 d-flex flex-column">
                    <div class="flex-grow-1 d-flex flex-column">
                        <ChatArea/>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Home
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import Message from './Message';
import MessageInput from './MessageInput';

function ChatArea() {
    return (
      <div className="card h-100 border-0 shadow-sm p-3 mb-5 bg-body-tertiary rounded " >
        <div className="card-header">
          <a href="{% url 'group_profile' group.id %}">
            <img
              src=""
              alt="profile"
              style={{ width: 60, height: 60, borderRadius: 30 }}
            />
          </a>
          <h3 className="card-title mb-1" style={{ display: "inline-block" }}>
            Group
          </h3>
          <br />
          <small className="text-muted">discription</small>
          <div>
            <p>4 members</p>
          </div>
        </div>
        <div className="card-body d-flex flex-column p-3">
          <div className="flex-grow-1 overflow-auto pb-5" style={{ maxHeight: "calc(100vh - 297px)" }}>
            <Message/>
            <Message/>
            <Message/>
            <Message/>
            <Message/>
            <Message/>
          </div>
        </div>
        <MessageInput/>
      </div>
    );
}
export default ChatArea;
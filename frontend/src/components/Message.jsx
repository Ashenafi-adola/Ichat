import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

function Message() {
    return (
      <div className="mb-2" >
        <div className="card p-2 border-1 shadow-sm">
          <div className="card-body p-0" style={{backgroundColor:"white"}}>
            <div className="d-flex justify-content-between align-items-center mb-2">
              <div className="d-flex align-items-center">
                <div
                  className="avatar bg-info text-white rounded-circle d-flex align-items-center justify-content-center me-3"
                  style={{
                    width: 25,
                    height: 25,
                    fontWeight: "bold",
                    display: "inline-block",
                  }}
                >
                  A
                </div>
                <strong className="text-primary">@ashenafi</strong>
              </div>
              <div>
                <small className="text-muted">10 days ago</small>
              </div>
            </div>
            <div className="message-body mb-2">
              <p className="mb-0 text-dark" style={{ fontSize: '0.9rem' }}>
                Lorem Ipsum is simply dummy text of the printing and typesetting
                industry.
              </p>
            </div>
            <div className="d-flex gap-2">
              <a href="#" className="btn btn-outline-info" style={{ fontSize: '0.75rem', padding: '0.15rem 0.4rem' }}>
                Edit
              </a>
              <a href="#" className="btn btn-outline-warning" style={{ fontSize: '0.75rem', padding: '0.15rem 0.4rem' }}>
                Delete
              </a>
            </div>
          </div>
        </div>
      </div>
    );
}

export default Message;
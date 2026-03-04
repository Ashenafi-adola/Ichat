import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

function Message() {
    return (
      <div className="mb-2">
        <div className="card p-2">
          <div className="card-body p-2">
            <div className="d-flex justify-content-between align-items-center mb-2">
              <div>
                <div
                  className="avatar bg-primary text-white rounded-circle d-flex align-items-center justify-content-center me-3"
                  style={{
                    width: 25,
                    height: 25,
                    fontWeight: "bold",
                    display: "inline-block",
                  }}
                >
                  A
                </div>
                <strong className="text-dark">@ashenafi</strong>
              </div>
              <div>
                <small className="text-muted">10 days ago</small>
              </div>
            </div>
            <div className="message-body mb-2">
              <p className="mb-0">
                Lorem Ipsum is simply dummy text of the printing and typesetting
                industry.
              </p>
            </div>
            <div className="d-flex gap-2">
              <a href="#" className="btn btn-sm btn-outline-primary">
                Edit
              </a>
              <a href="#" className="btn btn-sm btn-outline-danger">
                Delete
              </a>
            </div>
          </div>
        </div>
      </div>
    );
}

export default Message;
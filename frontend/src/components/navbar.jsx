import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

function NavBar() {
    return (
      <nav className="navbar navbar-dark bg-dark fixed-top">
        <div className="container-fluid">
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="offcanvas"
            data-bs-target="#offcanvasDarkNavbar"
            aria-controls="offcanvasDarkNavbar"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon" />
          </button>
          <a className="navbar-brand" href="#">I-CHAT</a>
          <div className="offcanvas offcanvas-start text-bg-dark" tabIndex={-1} id="offcanvasDarkNavbar" aria-labelledby="offcanvasDarkNavbarLabel" style={{width:"300px"}}>
            <div className="offcanvas-header">
              <h1>ICHAT</h1>
              <button type="button" className="btn-close btn-close-white" data-bs-dismiss="offcanvas" aria-label="Close"/>
            </div>
            <div className="offcanvas-body">
              <ul className="navbar-nav justify-content-end flex-grow-1 pe-3">
                <li className="nav-item">
                  <a className="nav-link active" aria-current="page" href="#">
                    All
                  </a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="#">
                    Friends
                  </a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="#">
                    Groups
                  </a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="#">
                    Channels
                  </a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="#">
                    Owed Groups
                  </a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="#">
                    Owed Channels
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </nav>
    );
  }

export default NavBar
function LogInPage() {
    return (
        <div className="d-flex justify-content-center align-items-center vh-100">   
        <form className="row g-3 border rounded p-4 shadow-sm" style={{ width: "420px" }}>
                <h1 className="text-center">Sign In</h1>
                <p className="text-center text-muted">Welcome back to I-CHAT</p>
                
                <div className="col-md-12">
                    <label htmlFor="inputEmail4" className="form-label">Username</label>
                    <input 
                        type="text" 
                        className="form-control" 
                        id="inputEmail4" 
                        placeholder="Enter username"
                    />
                </div>
                
                <div className="col-md-12">
                    <label htmlFor="inputPassword4" className="form-label">Password</label>
                    <input 
                        type="password" 
                        className="form-control" 
                        id="inputPassword4" 
                        placeholder="Enter password"
                    />
                </div>
                
                <div className="col-12 d-grid">
                    <button type="submit" className="btn btn-primary">Sign in</button>
                </div>
            </form>
        </div>
    );
}

export default LogInPage;
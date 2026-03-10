function LogInPage() {
    return (
        <div className="d-flex justify-content-center bg-light align-items-center vh-100" style={{}}>   
            <form className="row g-3 border rounded p-4 shadow-sm" style={{ width: "400px" }}>
                <h1 className="text-center">Sign In</h1>
                <p className="text-center text-muted">Welcome back to I-CHAT</p>
                <hr className="m-0"/>
                <div class="form-floating mb-3">
                    <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com"/>
                    <label for="floatingInput">Email address</label>
                </div>
                <div class="form-floating">
                    <input type="password" class="form-control" id="floatingPassword" placeholder="Password"/>
                    <label for="floatingPassword">Password</label>
                </div>
                
                <div className="col-12 d-grid">
                    <button type="submit" className="btn btn-primary">Sign in</button>
                </div>
                <div>
                    <p>Don't Have an account? 
                        <a href="">Create One.</a>
                    </p>
                </div>
            </form>
        </div>
    );
}

export default LogInPage;
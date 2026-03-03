function LogInPage(){
    return (
        <div class="d-flex justify-content-center">   
            <form class="row g-3 col-6 border rounded p-4 shadow-sm">
                <h1 class="text-center">Sign In</h1>
                <p class="text-center">Welcome back to I-CHAT</p>
                <div class="col-md-12 ">
                    <label for="inputEmail4" class="form-label ">Username</label>
                    <input type="text" class="form-control fixed-width-input" id="inputEmail4"></input>
                </div>
                <div class="col-md-12 ">
                    <label for="inputPassword4" class="form-label">Password</label>
                    <input type="password" class="form-control" id="inputPassword4"></input>
                </div>
                <div class="col-12">
                    <button type="submit" class="btn btn-primary">Sign in</button>
                </div>
            </form>
        </div>
    )
}

export default LogInPage;
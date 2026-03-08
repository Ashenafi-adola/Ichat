function MessageInput(){
    return(
        <div className="card-footer h-auto p-0">
          <form action="">
            <div class="input-group mb-3 p-0">
                <input type="text" className="form-control" placeholder="Type Your Message Here..." aria-label="Recipient’s username" aria-describedby="button-addon2"/>
                <button className="btn btn-outline-secondary" type="button" id="button-addon2">Send</button>
            </div>
          </form>
        </div>
    );
}

export default MessageInput;
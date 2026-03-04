function MessageInput(){
    return(
        <div className="card-footer">
          <form action="">
            <div class="input-group mb-3">
                <input type="text" class="form-control" placeholder="Type Your Message Here..." aria-label="Recipient’s username" aria-describedby="button-addon2"/>
                <button class="btn btn-outline-secondary" type="button" id="button-addon2">Send</button>
            </div>
          </form>
        </div>
    );
}

export default MessageInput;
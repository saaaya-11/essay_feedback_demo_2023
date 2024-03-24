window.onload = function() {
    var element = document.querySelector('msg_history');
    element.scrollTop = element.scrollHeight;
  };
  
/*
const Balloon_GPT={
    template: '<div class="msg_incoming"><div class="msg_image"> <img src="{% static "img/loading_bot.gif" %}" alt="sunil"></div><div class="msg_received"><div class="msg_received_withd"><p>{{message}}</p></div></div></div>',
    props: {
        message:{
            type:String,
            required: true
        }
    }
};

const Balloon_USER={
    template: '<div class="msg_outgoing"><div class="msg_sent"><p>返信ダミー</p></div></div>',
    props: {
        message:{
            type:String,
            required: true
        }
    }
};


const ChatForm={
    template: '<div class="msg_type"><div class="msg_write"><input type="text" class="msg_writer" placeholder="メッセージ"><button class="msg_send_btn" type="button">→</button></div></div>',
    props:{
        applyEvent:{
            type: String,
            required: true
        }
    },
    data(){
        return{
            message:''
        }
    },
    methods:{
        submit(){
            this.$emit(this.applyEvent, this.message)
            this.message=''
        }
    }
};
*/
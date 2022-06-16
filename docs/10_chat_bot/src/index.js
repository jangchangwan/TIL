// index.js

'use strict';

const socket = io();
const chatWindow = document.getElementById('chatWindow');
const sendButton = document.getElementById('chatMessageSendBtn');
const chatInput = document.getElementById('chatInput');

socket.on('connect', function(){
    const name = prompt('대화명을 입력해주세요.', '');
    socket.emit('newUserConnect', name);
});

socket.on('updateMessage', function(data){
    if(data.name === 'SERVER'){
        const info = document.getElementById('info');
        info.innerHTML = data.message;

        const chatMessageEl = drawChatMessage(data);
        chatWindow.appendChild(chatMessageEl);
        chatWindow.scrollTop = chatWindow.scrollHeight;
        // console.log(data.userList)
        updateUserList(data.userList)
        
        setTimeout(() => {
            info.innerText = '';
        }, 1000);


    }else{
        const chatMessageEl = drawChatMessage(data);
        chatWindow.appendChild(chatMessageEl);

        chatWindow.scrollTop = chatWindow.scrollHeight;
    }
});

sendButton.addEventListener('click', function(){
    const message = chatInput.value;

    if(!message) return false;
   
    socket.emit('sendMessage', {
        message
    });

    chatInput.value = '';
});

function updateUserList(userList){
    $('#userList').text('');
    let i
    for (i = 0; i < userList.length; i++){
        console.log(userList[i])
        $('#userList').append($('<li>').text(userList[i]));
    };
}

function drawChatMessage(data){
    const wrap = document.createElement('p');
    const message = document.createElement('span');
    const name = document.createElement('span');

    name.innerText = data.name;
    message.innerText = data.message;

    name.classList.add('output__user__name');
    message.classList.add('output__user__message');

    wrap.classList.add('output__user');
    wrap.dataset.id = socket.id;

    wrap.appendChild(name);
    wrap.appendChild(message);

    return wrap;
}
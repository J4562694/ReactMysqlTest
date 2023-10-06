import React, { useState } from 'react'
import { apiUrl } from './components/apiUrl'

const Login = () => {

    // catch account and password
    const [setAccount, addAccountHandle] = useState("")
    const [setPassword, addPasswordHandle] = useState("")

    // 表單送出
    const buttonSubmitHandle = async () =>{

        // 如果帳號或密碼為空
        if(setAccount === ""){
            alert("請輸入帳號")
            return
        }
        
        if(setPassword === ""){
            alert("請輸入密碼")
            return
        }

        fetch("${apiUrl}/login", {
            method : 'POST', 
            headers : {
                'Content-Type' : 'application/json'
            },
            credentials : 'include',
            body : JSON.stringify({password : setPassword}),
        })
        .then(response => {
            if (response.status === 201){
                console.log("原神，啟動!")
            }
        })
        .catch(error => console.log(error))

    }

  return (
    <>
        <form>

            <input
            type='text'
            id='addAccount'
            onChange={(e) => {
                addAccountHandle(e.target.value)
            }}
            placeholder='輸入帳號'
            />

            <input
            type='text'
            id='addPassword'
            onChange={(e) => {
                addPasswordHandle(e.target.value)
            }}
            placeholder='輸入密碼'
            />

            <button
            type='button'
            onClick={
                buttonSubmitHandle
            }>
                啟動!
            </button>
        </form>
    </>
  )
}

export default Login
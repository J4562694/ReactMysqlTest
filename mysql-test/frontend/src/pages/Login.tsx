import React, { useState } from 'react'
import { APIURL } from './components/apiUrl'

const Login = () => {

    // catch account and password
    const [setAccount, addAccountHandle] = useState("")
    const [setPassword, addPasswordHandle] = useState("")

    // 創建帳戶
    const [setCreateAccount, addCreateAccount] = useState("")
    const [setCreatePassword, addCreatePassword] = useState("")

    // 表單送出
    const buttonSubmitHandle = async () => {

        // 如果帳號或密碼為空
        if (setAccount === "") {
            alert("請輸入帳號")
            return
        }

        if (setPassword === "") {
            alert("請輸入密碼")
            return
        }

        fetch(`${APIURL}/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            credentials: 'include',
            body: JSON.stringify({ password: setPassword }),
        })
            .then(response => {
                if (response.status === 201) {
                    console.log("登入成功!")
                }
            })
            .catch(error => console.log(error))

    }

    const createSubmitButton = async () => {

        // 如果帳號或密碼為空
        if (setCreateAccount === "") {
            alert("請輸入帳號")
            return
        }

        if (setCreatePassword === "") {
            alert("請輸入密碼")
            return
        }

        

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

            <h1>你還沒有加入嗎!?</h1>
            <form>

                <input
                    type='text'
                    id='createAccount'
                    onChange={(e) => {
                        addCreateAccount(e.target.value)
                    }}
                    placeholder='輸入帳號'
                />

                <input
                    type='text'
                    id='createPassword'
                    onChange={(e) => {
                        addCreatePassword(e.target.value)
                    }}
                    placeholder='輸入密碼'
                />

                <button
                    type='button'
                    onClick={
                        createSubmitButton
                    }>
                    點擊加入!
                </button>
            </form>
        </>
    )
}

export default Login
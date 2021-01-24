import React, {useState} from 'react'
import {Typography, Input, Button} from 'antd'
const {Search} = Input
const aboutStyle = {
    height: "100vh",
    justifyContent: "center",
    alignItem: "center",
    margin: "auto 0",
}
const smaller = {
    paddingLeft: "15vw",
    paddingRight: "15vw"
}
const header = {
    color: "#b7e3fa",
    textAlign: "center",
    paddingTop: "30vh",
    fontSize: "6em"
}
export default function About() {
    const [username, SetUsername] = useState("")
    const onSearch = function(){
        const val = username
        console.log(username)
        SetUsername("")
    }
    return (
        <div style = {aboutStyle} >
          <Typography.Title style = {header}> Welcome to BadGIF <br/> Whats your username? </Typography.Title>
          <Search enterButton="Search" size = "large" style = {smaller}placeholder="input search text" value = {username} onSearch={onSearch} onChange = {(e) => SetUsername(e.target.value)} enterButton />
        </div >
    )
}

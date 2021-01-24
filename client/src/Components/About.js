import React from 'react'
import {Typography} from 'antd'
const aboutStyle = {
    height: "100vh",
    justifyContent: "center",
    alignItem: "center"
}
export default function About() {
    return (
        <div style = {aboutStyle} >
          <Typography.Title style = {{color: "#b7e3fa"}}>Hello I hate everything </Typography.Title>
        </div >
    )
}

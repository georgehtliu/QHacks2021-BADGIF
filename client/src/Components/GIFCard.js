
import {Card} from 'antd'
import 'antd/dist/antd.css';
import React from 'react'

export default function GIFCard(props) {
    const moodColor = props.mood <= 0 ? '#86C67C' : '#ff9999'

    return (
        <>
            <Card title = {props.user} style ={{display: 'grid', width:300, margin:10}} bordered = {true} 
            hoverable={true} 
            headStyle={{backgroundColor:moodColor}}
            bodyStyle={{backgroundColor:moodColor, color: "black", fontSize: "1.5em"}}>
                Mood: {props.mood} <br/>
                "{props.message}"

            </Card>
        </>
    )
}

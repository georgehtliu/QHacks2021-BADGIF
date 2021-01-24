
import {Card} from 'antd'
import 'antd/dist/antd.css';
import React from 'react'

export default function GIFCard(props) {
    const moodColor = props.mood <= 0 ? '#86C67C' : '#ff9999'

    return (
        <>
            <Card title = {props.user}
            headStyle={{backgroundColor:moodColor}}
            bodyStyle={{backgroundColor:moodColor}}>
                Mood: {props.mood}
                Message: {props.message}
            </Card>
        </>
    )
}

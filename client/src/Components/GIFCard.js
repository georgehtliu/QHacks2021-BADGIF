
import {Card} from 'antd'
import 'antd/dist/antd.css';
import React from 'react'

export default function GIFCard(props) {

    const hslToHex = (h, s, l) => {
        l /= 100;
        const a = s * Math.min(l, 1 - l) / 100;
        const f = n => {
          const k = (n + h / 30) % 12;
          const color = l - a * Math.max(Math.min(k - 3, 9 - k, 1), -1);
          return Math.round(255 * color).toString(16).padStart(2, '0');   // convert to Hex and prefix "0" if needed
        };
        return `#${f(0)}${f(8)}${f(4)}`;
    }

    
    const moodColor = (moodvalue) => {
        var hue=(((1-moodvalue)/2)*120).toString(10)
        return hslToHex(hue, 60, 50)
    }

    return (
        <>
            <Card title = {props.user} style ={{display: 'grid', width:300, margin:10}} bordered = {true} 
            hoverable={true} 
            headStyle={{backgroundColor:moodColor(props.mood)}}
            bodyStyle={{backgroundColor:moodColor(props.mood), color: "black", fontSize: "1.5em"}}>
                Mood: {props.mood} <br/>
                "{props.message}"

            </Card>
        </>
    )
}

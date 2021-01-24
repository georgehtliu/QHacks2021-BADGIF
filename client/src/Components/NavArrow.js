import React from 'react'
import { DoubleRightOutlined } from '@ant-design/icons'
import {Space} from 'antd'
export default function NavArrow() {
    return (
        <div style = {{textAlign: 'center'}}>
            <Space style={{ justifyContent: 'center' }}><a
                href={'#moods'}><DoubleRightOutlined rotate='90'
                    className="vert-move"
                    style={{
                        fontSize: 'max(12px,4em)',
                        marginTop: '5vw',
                    }} /></a></Space>
        </div>
    )
}

import React from 'react'
import { Card, Col, Row } from 'antd';
import GIFCard from './GIFCard'  
import 'antd/dist/antd.css';
export default function Cards() {
    return (
      <div className="site-card-wrapper">
      <GIFCard mood = {-1} user = "yobama"/>
      <GIFCard mood = {1} user = "yobama"/>
    </div>
    )
}

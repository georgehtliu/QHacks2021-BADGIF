import React from "react";
import { Card, Col, Row } from "antd";
import GIFCard from "./GIFCard";
import "antd/dist/antd.css";
import { useSelector } from "react-redux";
import {Masonry} from 'masonic'


export default function Cards() {
  const posts = useSelector((state) => state.posts);
  console.log(posts);

  
  const items = posts.map((post) => ({
    timestamp: post.timestamp,
    mood: post.mood,
    username: post.username,
    message: post.message,
  }))
  console.log(items)

  const EasyMasonryComponent = (props) => (
    <Masonry columnCount={4} items={items} render={MasonryCard} />
  )

  const MasonryCard = ({index, data: {timestamp, mood, username, message}, width}) => (
    <div key={timestamp}>
      <GIFCard
        mood={mood}
        user={username.replace("_", "#")}
        message={message}
      />
    </div>
    // <div>
    //   <h1>Mood: {mood}</h1>
    //   <div>User: {username.replace("_", "#")}</div>
    //   <div>Timestamp: {timestamp}</div>
    //   <div>Message: {message}</div>
    // </div>
  )

  return (
    <div id="moods" style={{display: 'flex', flexWrap: 'wrap', justifyContent: 'center'}}>
      <EasyMasonryComponent />
      {/* {posts.map((post) => (

        <div key={post.timestamp}>
          <GIFCard
            mood={post.mood}
            user={post.username.replace("_", "#")}
            message={post.message}
          />
        </div>
      ))} */}
    </div>
  );
}

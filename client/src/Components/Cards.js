import React from "react";
import { Card, Col, Row } from "antd";
import GIFCard from "./GIFCard";
import "antd/dist/antd.css";
import { useSelector } from "react-redux";

export default function Cards() {
  const posts = useSelector((state) => state.posts);
  console.log(posts);
  return (
    <div id="moods" style={{display: 'flex', flexWrap: 'wrap', justifyContent: 'center'}}>
      {posts.map((post) => (

        <div key={post.timestamp}>
          <GIFCard
            mood={post.mood}
            user={post.username.replace("_", "#")}
            message={post.message}
          />
        </div>
      ))}
    </div>
  );
}

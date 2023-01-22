import "./App.css";
import LogInForm from "./components/LogInForm";
import MyDiary from "./components/MyDiary";
import SpotifyWebApi from "spotify-web-api-js";
import { useState, useEffect } from "react";
import { Route } from 'react-router-dom';

function App() {
  // const spotifyApi = new SpotifyWebApi();
  // spotifyApi.setAccessToken("ebda86342f1f4cdd94ae46612d5318c5");
  
  // const searchMusic = async () => {
  //   const searchResults = await spotifyApi.search("sad", ["playlist"]);
  //   console.log(searchResults);
  // }
  // useEffect(()=> {
  //   console.log("in App's useEffect");
  //   searchMusic();
  // })
  return (
    <div className="App">
      {/* <Route path="/" exact component={MyDiary} />
      <Route path="/login" component={LogInForm} />
      <Route path="/my-entries" component={MyDiary} />
      <Route path="/my-music" component={MyDiary} /> */}
      {/* <h2>Welcome Back</h2>
      <LogInForm></LogInForm> */}
      <MyDiary />
    </div>
  );
}

export default App;

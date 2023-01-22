import LoadMusicButton from "./LoadMusicButton";
import Card from "./UI/Card";
import styles from "./DiaryForm.module.css";
import { useEffect, useState } from "react";
import axios from 'axios';



const DiaryForm = (props) => {
  const [enteredManualDiary, setEnteredManualDiary] = useState(null);
  const [enteredFile, SetEnteredFile] = useState(null);

  function convertToDataURLviaCanvas(url, callback, outputFormat) {
    var img = new Image();
    img.crossOrigin = "Anonymous";
    img.onload = function () {
      var canvas = document.createElement("CANVAS");
      var ctx = canvas.getContext("2d");
      var dataURL;
      canvas.height = this.height;
      canvas.width = this.width;
      ctx.drawImage(this, 0, 0);
      dataURL = canvas.toDataURL(outputFormat);
      callback(dataURL);
      canvas = null;
    };
    img.src = url;
  }

  const manualDiaryInputChangeHandler = (event) => {
    setEnteredManualDiary(event.target.value);
    console.log(enteredManualDiary);
  };

  const enteredFileInputChangeHandler = (event) => {
    SetEnteredFile(event.target.files[0]);
    console.log(event.target.files[0]);
  };

  const fetchMusicHandler = async (event) => {
    event.preventDefault();
    //send diary data to backend and get emotions
    //send request to music api and get songs
    //as the state changes, useEffect should update context for mood list and draw song, album, etc.
    console.log(event.target);
    // axios({
    //   method: 'post',
    //   url: '/user/12345',
    //   data: {
    //     FormData: fd;
    //   }
    // });
  };

  useEffect(() => {
    if (enteredFile != null) {
      console.log(enteredFile);
      // console.log("value", event.target.value);
  
      // reader.addEventListener("load", () => {
      //     console.log(reader.result);
      // })
      const fd = new FormData();
      fd.append("uploadedFile", enteredFile, enteredFile.name);
      console.log("formdata is", fd);
      axios.post("http://127.0.0.1:8000/diaries",fd);
    }
  }, [enteredFile]);

  return (
    <form onSubmit={fetchMusicHandler}>
      <Card>
        <h3>tell us about your day</h3>
        <textarea
          name="ManualDiary"
          id="ManualDiary"
          cols="30"
          rows="25"
          onChange={manualDiaryInputChangeHandler}
        ></textarea>
        <input
          onChange={enteredFileInputChangeHandler}
          type="file"
          accept=".png,.jpeg,.jpg"
        />
      </Card>
      <LoadMusicButton />
    </form>
  );
};
export default DiaryForm;

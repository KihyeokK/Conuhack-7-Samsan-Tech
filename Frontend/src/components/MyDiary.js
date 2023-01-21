import DiaryList from "./DiaryList";
import DiaryForm from "./DiaryForm";
import Navbar from "./UI/Navbar";
import styles from './MyDiary.module.css';
import { useState, useEffect } from "react";

const MyDiary = (props) => {

  const [clickedDiaryEntry, setClickedDiaryEntry] = useState({});

  const diaryClickHandler = (diaryEntry) => {
    setClickedDiaryEntry(diaryEntry);
  }

  return (
    <>
      <Navbar />
      <main className={styles["main-diary"]}>
        <DiaryList onDiaryClick={diaryClickHandler}/>
        <DiaryForm></DiaryForm>
      </main>
    </>
  );
};

export default MyDiary;

import DiaryList from "./DiaryList";
import DiaryForm from "./DiaryForm";
import SpecificDiaryEntry from "./SpecificDiaryEntry";
import Navbar from "./UI/Navbar";
import styles from './MyDiary.module.css';
import { useState, useEffect } from "react";

const MyDiary = (props) => {
  const [clickedDiaryEntry, setClickedDiaryEntry] = useState(null);

  const diaryClickHandler = (diaryEntry) => {
    setClickedDiaryEntry(diaryEntry);
    console.log(clickedDiaryEntry);
  }

  return (
    <>
      <Navbar />
      <main className={styles["main-diary"]}>
        <DiaryList onClick={diaryClickHandler}/>
        {clickedDiaryEntry ? <SpecificDiaryEntry diary={clickedDiaryEntry} /> : <DiaryForm />}
      </main>
    </>
  );
};

export default MyDiary;

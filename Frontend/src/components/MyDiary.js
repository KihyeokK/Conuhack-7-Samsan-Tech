import DiaryList from "./DiaryList";
import DiaryForm from "./DiaryForm";
import Navbar from "./UI/Navbar";
import styles from './MyDiary.module.css';

const MyDiary = (props) => {
  return (
    <>
      <Navbar />
      <main className={styles["main-diary"]}>
        <DiaryList />
        <DiaryForm></DiaryForm>
      </main>
    </>
  );
};

export default MyDiary;

import Card from "./UI/Card";

const SpecificDiaryEntry = (props) => {
    console.log(props.diary);
  return (
    <Card>
      <h3>{props.diary.date}</h3>
      <p>{props.diary.diary}</p>
      {props.diary.emotions}
      {props.diary.playListUrl}
    </Card>
  );
};

export default SpecificDiaryEntry;

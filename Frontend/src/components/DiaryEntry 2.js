const DiaryEntry = (props) => {
  const onLiClickHandler = () => {
    props.onClick({
      id: "4",
      diary: props.diary,
      date: props.date,
      isLiked: props.isLiked,
      emotions: props.emotions,
      playlistUrl: props.playlistUrl,
    });
    console.log("onclickHandler");
  };

  return (
    <li onClick={onLiClickHandler} className={props.className}>
      my mood on <span>{props.date}</span>
      <span>{props.isLiked}</span>
    </li>
  );
};

export default DiaryEntry;

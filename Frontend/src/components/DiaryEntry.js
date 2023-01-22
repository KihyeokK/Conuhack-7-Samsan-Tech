const DiaryEntry = (props) => {
  const onLiClickHandler = () => {
    props.onClick({
      id: props.id,
      content: props.content,
      created_at: props.created_at,
      is_liked: props.is_liked,
      mood: props.mood,
      music: props.music,
    });
    console.log("onclickHandler");
  };

  return (
    <li onClick={onLiClickHandler} className={props.className}>
      my mood on <span>{new Date(props.created_at).toDateString()}</span>
      <span>{props.is_liked}</span>
    </li>
  );
};

export default DiaryEntry;

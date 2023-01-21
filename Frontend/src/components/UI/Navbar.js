import styles from "./Navbar.module.css";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHeart, faChevronRight } from '@fortawesome/free-solid-svg-icons';
import { useState } from "react";


const Navbar = (props) => {
    const [isNavbarExpanded, setIsNavBarExpanded] = useState(false);

    const onExpandClickHandler = () => {
        setIsNavBarExpanded(true);
    }

  return (
    <nav className={styles.nav}>
      <ul className={styles['navbar-nav']}>
{/* <li className={isNavbarExpanded ? styles['nav-item'] : ''}> */}
        <li className={styles['nav-item']}>
          {/* use Link tag  */}
          <a href="#" className={styles['nav-link']}>
          <span className="link-text">My Diary</span>
          </a>
        </li>
        <li className={styles['nav-item']}>
          {/* use Link tag  */}
          <a href="#" className={styles['nav-link']}><span className="link-text">My Hearts</span></a>
        </li>
        <li className={styles['nav-item-arrow']}>
          {/* use Link tag  */}
          <FontAwesomeIcon icon={"fa-chevrons-right"} />
          <FontAwesomeIcon icon={['fal', 'code']} size="sm" />
          <button onClick={onExpandClickHandler}>
            <FontAwesomeIcon icon={faChevronRight} />
          </button>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;

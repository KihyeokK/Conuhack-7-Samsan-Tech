import styles from './LogInForm.module.css';

const LogInForm = (props) => {
  return (
    <form className={styles['login-form']}>
      <label htmlFor="email">Email Address</label>
      <input
      className={styles['input-box']}
        type="email"
        id="email"
        name="email"
        placeholder="your email address"
      />
      <label htmlFor="password">Password</label>
      <input
      className={styles['input-box']}
        type="password"
        id="password"
        name="password"
        placeholder="your password"
      />
      <label htmlFor="rememberMe">Remember Me</label>
      <input type="checkbox" id="rememberMe" name="rememberMe" />
      <button type="submit">log in</button>
    </form>
  );
};

export default LogInForm;

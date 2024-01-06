import React from "react";
import styles from "./styles/LoginForm.module.css";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { validateLoginForm } from "./utils/validateLoginForm";
import { toast } from "react-toastify";
import { errorConfig } from "../../config/toasts";

export default function LoginForm() {
  const navigate = useNavigate();

  const redirect = (event: React.MouseEvent<HTMLAnchorElement, MouseEvent>) => {
    event.preventDefault();
    navigate("/signup");
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    const formData = new FormData(e.currentTarget);
    const hasErrors = validateLoginForm(formData);
    if (hasErrors) return;

    const body = {
      login: formData.get("login"),
      password: formData.get("password"),
    };

    const toastID = toast.loading("Please wait...");

    try {
      await axios.post(`${process.env.REACT_APP_SERVER_URL}/auth/login`, body, {
        withCredentials: true,
      });

      toast.dismiss(toastID);
      navigate("/");
    } catch (e) {
      toast.update(
        toastID,
        errorConfig("An error occured when logging in. Check your credentials.")
      );
    }
  };

  return (
    <form className={styles.form} onSubmit={handleSubmit}>
      <h2 className={styles.h2}>login</h2>
      <input
        type="text"
        name="login"
        placeholder="login"
        className={styles.input}
      />
      <input
        type="password"
        name="password"
        placeholder="password"
        className={styles.input}
      />
      <button type="submit" className={styles.button}>
        login
      </button>
      <p className={styles.p}>
        Don't have account? Sign up{" "}
        <a onClick={redirect} href="/signup">
          here
        </a>
        .
      </p>
    </form>
  );
}

import { toast } from "react-toastify";

export const validateForm = (formData: FormData): boolean => {
  const login = formData.get("login");
  const password = formData.get("password");
  const confirmPassword = formData.get("confirmPassword");
  const username = formData.get("username");
  const avatar = formData.get("avatar") as File;

  let hasError = false;

  if (!avatar.name) {
    toast.error("No avatar given.");
    hasError = true;
  }

  if (!username) {
    toast.error("No username given.");
    hasError = true;
  }

  if (!login) {
    toast.error("No login given.");
    hasError = true;
  }

  if (!password) {
    toast.error("No password given.");
    hasError = true;
  }

  if (!confirmPassword) {
    toast.error("No password confirmation given.");
    hasError = true;
  }

  if (confirmPassword !== password) {
    toast.error("Passwords don't match.");
    hasError = true;
  }

  return hasError;
};

import { toast } from "react-toastify";

export const validateLoginForm = (formData: FormData): boolean => {
  const login = formData.get("login");
  const password = formData.get("password");

  let hasErrors = false;

  if (!login) {
    toast.error("No login given.");
    hasErrors = true;
  }

  if (!password) {
    toast.error("No password given.");
    hasErrors = true;
  }

  return hasErrors;
};

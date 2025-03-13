import { render, screen } from '@testing-library/react';
import Query from '../src/components/Query';

test('renders query input', () => {
  render(<Query />);
  const inputElement = screen.getByPlaceholderText(/Ask about compliance/i);
  expect(inputElement).toBeInTheDocument();
});
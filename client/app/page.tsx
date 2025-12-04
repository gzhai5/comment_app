import NavBar from "./components/navbar/navbar";
import Foobar from "./components/foobar/foobar";
import CommentWidget from "./components/comment/widget";

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen items-center bg-zinc-50 font-sans relative">
      <NavBar />
      <main className="p-6 flex-grow w-full flex-col items-center">
        <h1 className="mb-4 text-2xl font-bold text-gray-800">Comments</h1>
        <CommentWidget />
      </main>
      <Foobar />
    </div>
  );
}

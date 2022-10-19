from .models import User, Skill, UserType, WorkType, EmploymentType, Category, Job


class UserApi:
    @staticmethod
    def get(user_id):
        return User.objects.get(id=user_id)

    @staticmethod
    def all():
        return User.objects.all()

    @staticmethod
    def published_jobs(user_id):
        return User.objects.get(user_id).published_jobs

    @staticmethod
    def update(user_id, first_name, last_name, avatar_url, cv_url, location, phone_number):
        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.avatar_url = avatar_url
        user.cv_url = cv_url
        user.location = location
        user.phone_number = phone_number
        user.save()
        return user

    @staticmethod
    def delete(user_id):
        user = User.objects.get(id=user_id)
        user.delete()
        return user


class JobApi:
    @staticmethod
    def open(title, description, salary, deadline, category_id, company_id, work_type_id):
        job = Job()
        job.title = title
        job.description = description
        job.salary = salary
        job.deadline = deadline
        job.status = 1
        job.category = CategoryApi.get(category_id)
        job.company = UserApi.get(company_id)
        job.work_type = WorkTypeApi.get(work_type_id)
        job.save()
        return job

    @staticmethod
    def close(job_id):
        job = Job.objects.get(id=job_id)
        job.status = 2
        job.save()
        return job

    @staticmethod
    def get(job_id):
        return Job.objects.get(id=job_id)

    @staticmethod
    def all():
        return Job.objects.all()

    @staticmethod
    def delete(job_id):
        job = Job.objects.get(id=job_id)
        job.delete()
        return job


class CategoryApi:
    @staticmethod
    def create(name):
        category = Category.objects.create(name)
        category.save()
        return category

    @staticmethod
    def get(category_id):
        return Category.objects.get(id=category_id)

    @staticmethod
    def all():
        return Category.objects.all()

    @staticmethod
    def jobs(category_id):
        return Category.objects.get(id=category_id).jobs

    @staticmethod
    def update(category_id, name):
        category = Category.objects.get(id=category_id)
        category.name = name
        category.save()
        return category

    @staticmethod
    def delete(category_id):
        category = Category.objects.get(id=category_id)
        category.delete()
        return category


class SkillApi:
    @staticmethod
    def create(name):
        skill = Skill.objects.create(name)
        skill.save()
        return skill

    @staticmethod
    def get(skill_id):
        return Skill.objects.get(id=skill_id)

    @staticmethod
    def all():
        return Skill.objects.all()

    @staticmethod
    def seekers(skill_id):
        return Skill.objects.get(id=skill_id).user_set

    @staticmethod
    def update(skill_id, name):
        skill = Skill.objects.get(id=skill_id)
        skill.name = name
        skill.save()
        return skill

    @staticmethod
    def delete(skill_id):
        skill = Skill.objects.get(id=skill_id)
        skill.delete()
        return skill


class UserTypeApi:
    @staticmethod
    def create(name):
        user_type = UserType.objects.create(name)
        user_type.save()
        return user_type

    @staticmethod
    def get(user_type_id):
        return UserType.objects.get(id=user_type_id)

    @staticmethod
    def all():
        return UserType.objects.all()

    @staticmethod
    def update(user_type_id, name):
        user_type = UserType.objects.get(id=user_type_id)
        user_type.name = name
        user_type.save()
        return user_type

    @staticmethod
    def delete(user_type_id):
        user_type = UserType.objects.get(id=user_type_id)
        user_type.delete()
        return user_type


class WorkTypeApi:
    @staticmethod
    def create(name):
        work_type = WorkType.objects.create(name)
        work_type.save()
        return work_type

    @staticmethod
    def get(work_type_id):
        return WorkType.objects.get(id=work_type_id)

    @staticmethod
    def all():
        return WorkType.objects.all()

    @staticmethod
    def update(work_type_id, name):
        work_type = WorkType.objects.get(id=work_type_id)
        work_type.name = name
        work_type.save()
        return work_type

    @staticmethod
    def delete(work_type_id):
        work_type = WorkType.objects.get(id=work_type_id)
        work_type.delete()
        return work_type


class EmploymentTypeApi:
    @staticmethod
    def create(name):
        employment_type = EmploymentType.objects.create(name)
        employment_type.save()
        return employment_type

    @staticmethod
    def get(employment_type_id):
        return EmploymentType.objects.get(id=employment_type_id)

    @staticmethod
    def all():
        return EmploymentType.objects.all()

    @staticmethod
    def update(employment_type_id, name):
        employment_type = EmploymentType.objects.get(id=employment_type_id)
        employment_type.name = name
        employment_type.save()
        return employment_type

    @staticmethod
    def delete(employment_type_id):
        employment_type = EmploymentType.objects.get(id=employment_type_id)
        employment_type.delete()
        return employment_type
